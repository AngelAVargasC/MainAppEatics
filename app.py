from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

DATABASE = 'DB_CAT_SKU.db'
UPLOAD_FOLDER = 'uploads'


# Crear la carpeta de uploads si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                Nombre TEXT,
                Nombre_para_mostrar TEXT,
                Precio_en_línea REAL,
                Clave_de_Producto_Servicio_SAT TEXT,
                CLAVE_DE_UNIDAD_NSSAT TEXT,
                CLAVE_DE_UNIDAD_SAT TEXT,
                SKU_LIVERPOOL TEXT,
                Precio_a_clientes_en_línea REAL,
                Artículo_de_matriz TEXT,
                Artículo_miembro TEXT,
                Tipo TEXT,
                Submarca TEXT,
                Producto TEXT,
                Genero TEXT,
                UNIDAD_DE_NEGOCIO TEXT,
                TEMPORADA TEXT,
                AÑO INTEGER,
                MES INTEGER,
                IEAN TEXT,
                COLOR TEXT,
                Talla TEXT,
                ID_externo TEXT,
                Tipo_2 TEXT,
                Marca TEXT,
                Latam_MX_Clave_ProdServSAT TEXT,
                Latam_MX_Clave_UnidadSAT TEXT,
                Latam_MX_UnidadSAT TEXT,
                Programa_fiscal TEXT,
                Código_de_proveedor TEXT,
                Nombre_de_la_empresa TEXT,
                Unidades_por_Empaque INTEGER,
                Precio_del_proveedor REAL,
                Nombre_2 TEXT,
                Hi INTEGER,
                Ti INTEGER,
                ID_externo_2 TEXT,
                Latam_MX_Item TEXT,
                SKU_LIVERPOOL_2 TEXT,
                Latam_MX_Codigo_Addenda TEXT,
                Latam_MX_Tipo_Addenda TEXT,
                IEAN_2 TEXT,
                SKU_CHEDRAUI TEXT,
                Peso_Bruto_por_Pieza REAL,
                Peso_Neto_por_Pieza REAL,
                Peso_Bruto_de_Empaque REAL,
                Peso_Neto_de_Empaque REAL,
                SKU_SORIANA TEXT,
                Latam_MX_Clave_ProdServSAT_2 TEXT,
                Latam_MX_Clave_UnidadSAT_2 TEXT,
                Latam_MX_UnidadSAT_2 TEXT,
                Unidad_de_ventas_principal TEXT,
                CFDI_4_0_Embalaje TEXT,
                CFDI_4_0_Peso_en_KG REAL,
                CFDI_4_0_Sat_clave_prod_servicio TEXT
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/pedidos')
def pedidos():
    return render_template('Pedidos.html')

@app.route('/cargar_excel', methods=['GET', 'POST'])
def cargar_excel():
    if request.method == 'POST':
        file = request.files['file']
        if file and (file.filename.endswith('.xls') or file.filename.endswith('.xlsx')):
            try:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                
                if file.filename.endswith('.xls'):
                    df = pd.read_excel(file_path, engine='xlrd')
                elif file.filename.endswith('.xlsx'):
                    df = pd.read_excel(file_path, engine='openpyxl')
                
                with sqlite3.connect(DATABASE) as conn:
                    df.to_sql('productos', conn, if_exists='append', index=False)
                
                os.remove(file_path)
                return redirect(url_for('pedidos'))
            except Exception as e:
                # Imprimir el error en la consola
                print(f"Error procesando el archivo: {e}")
                # Mostrar el error en la interfaz
                return f"Error procesando el archivo: {e}"
    return render_template('cargar_excel.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/opcion1')
def opcion1():
    return render_template('opcion1.html')

@app.route('/opcion2')
def opcion2():
    return render_template('opcion2.html')


@app.route('/opcion3')
def opcion3():
    return render_template('opcion3.html')

@app.route('/opcion4')
def opcion4():
    return render_template('opcion4.html')

@app.route('/opcion5')
def opcion5():
    return render_template('opcion5.html')

@app.route('/opcion6')
def opcion6():
    return render_template('opcion6.html')
if __name__ == '__main__':
    init_db()
    app.run(debug=True, host="0.0.0.0")
