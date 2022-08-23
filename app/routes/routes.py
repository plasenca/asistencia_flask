import datetime
import pandas as pd

from app import app
from flask import flash
from flask import Markup
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template
from constants import BASE_DIR, FILES_DIR
from psycopg2 import DatabaseError
from utilities import DataConverter
from utilities import DataManagment
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.utils import secure_filename
from models.models import FileLoader
from models.models import RegisterForms, Role
from models.models import LoginForm, PageRegisterForm


# Base URL redirect to login 
@app.route('/')
def index():
    return redirect("login"), 302

@app.route('/register', methods=["GET", "POST"])
def registro():

    form = PageRegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():

            register_user = {
                "email": form.email.data,
                "email_confirmed_at": datetime.datetime.now(),
                "password": form.password.data,
                "is_active": True,
                "first_name": form.first_name.data,
                "last_name": form.last_name.data,
                "work_id": form.work_id.data,
                "role_id": 2
            }
            
            # Verificando si el usuario ya ha sido creado
            user = RegisterForms.get_by_email(register_user["email"])
            if user is not None:
                error = Markup(f"El email \"<strong>{register_user['email']}</strong>\" ya está siendo usado por otro usuario")
                flash(error)
            else:
                user = RegisterForms(email=register_user["email"], 
                                    email_confirmed_at=register_user["email_confirmed_at"],
                                    password=register_user["password"],
                                    active=register_user["is_active"],
                                    first_name=register_user["first_name"],
                                    last_name=register_user["last_name"],
                                    work_id=register_user["work_id"],
                                    role_id=register_user["role_id"])
                user.set_password(register_user["password"])
                user.save()
                
                registration_success = "Registro Exitoso"
                flash(registration_success)
                return redirect(url_for("login")), 302
    return render_template('registro/registro.html', form=form), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('main')), 302
    
    form = LoginForm()    

    if request.method == "POST":
        if form.validate_on_submit():
            
            login_user_dict = {
                "email"   : form.email.data,
                "password": form.password.data,
                "remember": form.remember.data
            }
            user = RegisterForms.get_by_email(login_user_dict["email"])
            # Si el correo no existe
            if user is None:
                error = f"Usuario no encontrado"
                flash(error)
            else:
                # Si la contraseña concuerda con la ingresada
                if user.check_password(login_user_dict["password"]):
                    login_user(user, remember=login_user_dict["remember"])
                    return redirect(url_for("main")), 302
                else: 
                    error = f"La contraseña ingresada es  inválida"
                    flash(error)
    return render_template('login/login.html', form=form, request=request), 200

@app.route('/main', methods=["GET"])
@login_required
def main():
    form = FileLoader()
    path_file = FILES_DIR/"final_data.csv"
    # If it exists the csv file
    file = path_file if path_file.is_file() else None
    
    if file:
        file_csv = DataConverter._to_format_time(file, columns=["arrive_time"], format_time = "%Y-%m-%d %H:%M:%S")
    else:
        file_csv = None
    
    return render_template('main/main.html', form=form, file_csv=file_csv), 200

@app.route('/file-added', methods=["POST"])
@login_required
def file_added():
    
    form = FileLoader()
    data_manager = DataManagment()
    
    if form.validate_on_submit():
        
        file_oficina_principal = form.file_oficina_principal.data
        file_nicollini = form.file_nicollini.data
        file_ferretero = form.file_ferretero.data
        
        # Files Dicc
        dicc_files = {
            "oficina_principal": file_oficina_principal,
            "nicollini":file_nicollini,
            "ferretero": file_ferretero
        }
        
        # Conditionals
        files = file_oficina_principal or file_ferretero or file_nicollini
        
        # If it does exist any file
        if files:
            # Delete all files before adding another one
            deleted_files = data_manager._delete_files(FILES_DIR)
            
            # If it cannot delete files
            if deleted_files:
                # Store the file
                for name, file in dicc_files.items():
                    
                    if file:
                        
                        format_file = str(file.filename).split(".")[-1]
                        
                        # If format file is ".dat"
                        if format_file == "dat":
                            # filename = secure_filename(file.filename)
                            filename = f"{name}.dat"
                            file.save(FILES_DIR/filename)
                            
                        else:
                            flash("Must be .dat files")
                            return redirect(url_for("main")), 302
                        
                    else:
                        print(f"{name} es {file}")
                        
                return redirect(url_for("dat_converter")), 302
            
            else:
                flash("""There was an error uploading files. Please try again\n
                        If the error persists, contact support.""")
                raise BaseException(f"Failed to remove items from path: {FILES_DIR}")

        # If it does not exist any file
        if files is None:
            error = "Missing a file to upload"
            flash(error, category="error")
            return redirect(url_for("main")), 302


@app.route("/dat-converter", methods=["GET", "POST"])
@login_required
def dat_converter():
    
    # Get dicc paths
    datfiles_list = list(FILES_DIR.glob("*.dat"))
    datfiles_dicc = {data.name.split(".")[0]:data 
                    for data in datfiles_list}
    
    length_datfiles_list = datfiles_dicc.__len__()
    
    # Dataframes 
    df = None
    df_datfiles_list_newcolumn = []
    
    # Processing Dataframes
        # Tranform each ".dat" file to DataFrame
    for name, file in datfiles_dicc.items():
        
        # Adding new columns: "place"
        match name:
            case "oficina_principal":
                
                df_temporary = DataConverter._reader_dat(file)
                # df.insert(index column, name column, value to add, allow_duplicates=False )
                df_temporary.insert(2, "place", 2 ,allow_duplicates=False) # Es mutable
                df_datfiles_list_newcolumn.append(df_temporary) 
            case "nicollini":
                
                df_temporary = DataConverter._reader_dat(file)
                df_temporary.insert(2, "place", 3 ,allow_duplicates=False)
                df_datfiles_list_newcolumn.append(df_temporary) 
            case "ferretero":
                
                df_temporary = DataConverter._reader_dat(file)
                df_temporary.insert(2, "place", 4 ,allow_duplicates=False)
                df_datfiles_list_newcolumn.append(df_temporary)  

        # Delete useless columns
    index_columns = [[3,4,5,6]]*length_datfiles_list
    df_datfiles_deleted_columns_list = list(map(DataManagment.delete_columns_by_index, df_datfiles_list_newcolumn, index_columns))
    
    # If there's more than one file
    if length_datfiles_list > 1:
        for i in range(length_datfiles_list - 1):
            if df is None:
                df = pd.concat([df_datfiles_deleted_columns_list[i], df_datfiles_deleted_columns_list[i+1]], ignore_index=True)
            else:
                df = pd.concat([df, df_datfiles_deleted_columns_list[i+1]], ignore_index=True)
    else:
        df = df_datfiles_deleted_columns_list[0]
    
    # Sort and creating nedded columns: "month"
    df.columns = ["employee_id", "arrive_time", "location"]
    df["arrive_time"] = pd.to_datetime(df["arrive_time"], format="%Y-%m-%d %H:%M:%S")
        # Create month column: str | format: Str Month
    df["month"] = df["arrive_time"].apply(lambda m: m.strftime("%B"))
        # Create arrive_hour column: str | format = 00:00:00 AM/PM
    df["arrive_hour"] = df["arrive_time"].apply(lambda d: d.time().strftime(format="%X %p"))
    
    df.info()
    # Create a ".csv" file with the whole data converted
    df.to_csv(FILES_DIR/"final_data.csv")
    
    return redirect(url_for("main")), 302
    

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index")), 302

# Error Pages

@app.errorhandler(404)
def page_404(error):
    return render_template("errors/404.html"), 404

@app.errorhandler(DatabaseError)
def page_500(error):
    return render_template("errors/500.html"), 500


# Custom Filters

    # Custom Filter to convert str to datetime format
@app.template_filter('date')
def date_filter(s, format):
    return datetime.datetime.strptime(s, format)

    # Custom Filter to return the month form a datetime object
@app.template_filter('month')
def month_filter(s):
    return datetime.datetime.strftime(s, "%B")

    # 
@app.template_filter("strip")
def str_strip(s:str):
    return s.strip()