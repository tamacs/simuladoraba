import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Simulador de Abastecimiento", layout="wide")

# Inicializar variables de sesión si no existen
if "puntaje" not in st.session_state:
    st.session_state["puntaje"] = 0
if "etapa" not in st.session_state:
    st.session_state["etapa"] = 1  # Se inicializa correctamente

# Función para avanzar de etapa
def avanzar(puntos):
    st.session_state["puntaje"] += puntos
    st.session_state["etapa"] += 1

# Título principal
st.title("🛒 Simulador de Abastecimiento en SAP")

st.write("Bienvenido/a al simulador de abastecimiento. Debes tomar decisiones correctas para completar el proceso con éxito.")

# ETAPA 1: Detección de la necesidad
if st.session_state.get("etapa", 1) == 1:  # Usar .get() como refuerzo
    st.subheader("📌 Etapa 1: Detección de la Necesidad")
    st.write("Tu equipo necesita adquirir materiales para la oficina. ¿Qué tipo de bien o servicio necesitas?")
    
    if st.button("📄 Papelería"):
        avanzar(10)
    if st.button("💻 Software"):
        avanzar(5)  # Penalización porque requiere orden de compra

# ETAPA 2: Carga de Solicitud
elif st.session_state.get("etapa", 1) == 2:
    st.subheader("📌 Etapa 2: Carga de Solicitud")
    st.write("¿Dónde quieres cargar la solicitud de pedido?")
    
    if st.button("🖥️ SAP"):
        avanzar(10)
    if st.button("📋 Wrike"):
        avanzar(7)  # Alternativa válida pero no ideal

# ETAPA 3: Selección del Proveedor
elif st.session_state.get("etapa", 1) == 3:
    st.subheader("📌 Etapa 3: Selección del Proveedor")
    st.write("¿A qué proveedor eliges?")
    
    if st.button("✅ Proveedor Sugerido"):
        avanzar(10)
    if st.button("🆕 Nuevo Proveedor (no registrado)"):
        avanzar(5)  # Penalización porque tarda más

# ETAPA 4: Recepción del Bien o Servicio
elif st.session_state.get("etapa", 1) == 4:
    st.subheader("📌 Etapa 4: Recepción del Bien o Servicio")
    st.write("El proveedor ha entregado el pedido. ¿Todo llegó correctamente?")
    
    if st.button("✔️ Sí, todo correcto"):
        avanzar(10)
    if st.button("❌ No, hay errores"):
        avanzar(3)  # Penalización por gestionar correcciones

# ETAPA 5: Autorización del Gasto
elif st.session_state.get("etapa", 1) == 5:
    st.subheader("📌 Etapa 5: Autorización del Gasto")
    st.write("Debes autorizar el gasto. ¿Qué datos necesitas?")
    
    if st.button("📑 Orden de Compra, Importe, Fecha, Concepto"):
        avanzar(10)
    if st.button("📜 Solo Factura"):
        avanzar(5)  # Error porque faltan datos

# ETAPA 6: Pago al Proveedor
elif st.session_state.get("etapa", 1) == 6:
    st.subheader("📌 Etapa 6: Pago al Proveedor")
    st.write("El área de Administración ha procesado la factura y realizado el pago. ¡Misión cumplida!")

    st.write(f"Tu puntaje final es: **{st.session_state['puntaje']}** puntos")

    if st.session_state["puntaje"] >= 50:
        st.success("¡Muy bien! Seguiste correctamente el proceso.")
    else:
        st.warning("Revisa las mejores prácticas del proceso de abastecimiento para optimizar tiempos.")

    if st.button("🔄 Reiniciar Juego"):
        st.session_state["puntaje"] = 0
        st.session_state["etapa"] = 1
