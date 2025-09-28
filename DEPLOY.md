# Deploy en Streamlit Community Cloud

## Requisitos Previos

1. **Cuenta de GitHub**: Necesitas tener tu código en un repositorio de GitHub
2. **Cuenta de Streamlit**: Crear cuenta gratuita en [share.streamlit.io](https://share.streamlit.io)

## Preparación del Repositorio

### 1. Estructura de Archivos Necesaria

Asegúrate de que tu repositorio tenga esta estructura:

```
test_alejandro_marcano/
├── 1_Test_1_Funnel_Analysis.py        # Archivo principal (página de inicio)
├── pages/
│   ├── 2_Test_2_Instagram_Reels.py    # Página 2
│   └── 3_Test_3_SQL_Database.py       # Página 3
├── data_test1.csv                     # Datos para Test 1
├── data_test2.csv                     # Datos para Test 2
├── database_schema.sql                # Schema SQL para Test 3
├── requirements.txt                   # Dependencias de Python
└── README.md                          # Documentación del proyecto
```

### 2. Verificar requirements.txt

El archivo `requirements.txt` debe contener solo las dependencias esenciales:

```
pandas>=2.0.0
numpy>=1.24.0
streamlit>=1.28.0
plotly>=5.15.0
sqlalchemy>=2.0.0
```

**Nota importante**: `sqlite3` viene incluido con Python, no lo agregues a requirements.txt

### 3. Configurar la Base de Datos

Crea un archivo `setup_database.py` para inicializar la base de datos automáticamente:

```python
import sqlite3
import os

def setup_database():
    if not os.path.exists('ecommerce.db'):
        conn = sqlite3.connect('ecommerce.db')
        
        # Leer y ejecutar el schema SQL
        with open('database_schema.sql', 'r') as f:
            sql_script = f.read()
        
        conn.executescript(sql_script)
        conn.close()
        print("Database created successfully!")

if __name__ == "__main__":
    setup_database()
```

## Pasos para Deploy

### 1. Subir Código a GitHub

```bash
# Inicializar repositorio Git (si no existe)
git init

# Agregar archivos
git add .

# Hacer commit
git commit -m "Initial commit - Streamlit multipage app"

# Conectar con repositorio remoto
git remote add origin https://github.com/TU_USUARIO/test_alejandro_marcano.git

# Subir código
git push -u origin main
```

### 2. Deploy en Streamlit Community Cloud

1. **Ir a Streamlit Community Cloud**:
   - Visita [share.streamlit.io](https://share.streamlit.io)
   - Inicia sesión con tu cuenta de GitHub

2. **Crear Nueva App**:
   - Click en "New app"
   - Selecciona tu repositorio: `TU_USUARIO/test_alejandro_marcano`
   - **Branch**: `main`
   - **Main file path**: `1_Test_1_Funnel_Analysis.py`
   - **App URL**: `test-alejandro-marcano` (o el nombre que prefieras)

3. **Configuración Avanzada** (opcional):
   - **Python version**: 3.9 o superior
   - **Secrets**: No necesario para este proyecto

4. **Deploy**:
   - Click en "Deploy!"
   - Espera a que se complete el proceso (2-5 minutos)

### 3. Verificar el Deploy

Una vez completado, tu app estará disponible en:
```
https://TU_USUARIO-test-alejandro-marcano.streamlit.app
```

## Configuración Adicional

### Archivo .streamlit/config.toml (incluido)

El proyecto incluye configuración personalizada de Streamlit:

```toml
[theme]
# Optional: Custom theme colors (commented out)

[server]
headless = true
port = 8501

[browser]
gatherUsageStats = false

[client]
showErrorDetails = false
toolbarMode = "minimal"

[ui]
hideTopBar = true
```

**Características:**
- **Oculta elementos de Streamlit**: Fork button, GitHub links, "Made with Streamlit"
- **Toolbar mínimo**: Interfaz más limpia
- **Sin estadísticas**: No envía datos de uso a Streamlit
- **Top bar oculto**: Más espacio para contenido

### Secrets Management

Si necesitas variables de entorno o secrets:

1. En Streamlit Community Cloud, ve a tu app
2. Click en "Settings" → "Secrets"
3. Agrega tus secrets en formato TOML:

```toml
# Ejemplo de secrets
API_KEY = "tu_api_key_aqui"
DATABASE_URL = "tu_database_url"
```

## Solución de Problemas Comunes

### Error: "ModuleNotFoundError"
- Verifica que todas las dependencias estén en `requirements.txt`
- Usa versiones específicas si hay conflictos

### Error: "File not found"
- Asegúrate de que todos los archivos estén en el repositorio
- Verifica las rutas relativas en tu código

### Error de Base de Datos
- Incluye `database_schema.sql` en el repositorio
- Considera usar el script `setup_database.py` en el inicio de la app

### App muy lenta
- Optimiza el código con `@st.cache_data` para funciones pesadas
- Reduce el tamaño de los datasets si es posible

## Actualizar la App

Para actualizar tu app desplegada:

```bash
# Hacer cambios en tu código local
git add .
git commit -m "Update: descripción de cambios"
git push origin main
```

Streamlit Community Cloud detectará automáticamente los cambios y redesplegará la app.

## Monitoreo y Logs

- **Logs**: Disponibles en la interfaz de Streamlit Community Cloud
- **Métricas**: Puedes ver estadísticas de uso en el dashboard
- **Errores**: Los errores aparecen en tiempo real en los logs

## Límites de Streamlit Community Cloud

- **Recursos**: CPU y memoria limitados
- **Apps**: Máximo 3 apps públicas gratuitas
- **Almacenamiento**: 1GB por app
- **Tráfico**: Sin límite específico, pero uso razonable

## Enlaces Útiles

- [Documentación oficial de Deploy](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Community Cloud](https://share.streamlit.io)
- [Troubleshooting Guide](https://docs.streamlit.io/streamlit-community-cloud/troubleshooting)
