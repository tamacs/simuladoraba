import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Simulador de Abastecimiento", layout="wide")

# Inicializar variables de sesión
if "puntaje" not in st.session_state:
    st.session_state["puntaje"] = 0
if "etapa" not in st.session_state:
    st.session_state["etapa"] = 1
if "categoria" not in st.session_state:  # Para almacenar la elección inicial
    st.session_state["categoria"] = None

# Función para avanzar de etapa con control de errores
def avanzar(puntos, categoria=None):
    if categoria:  # Guardar la elección inicial solo si aún no ha sido elegida
        st.session_state["categoria"] = categoria
    st.session_state["puntaje"] += puntos
    st.session_state["etapa"] += 1
    st.experimental_rerun()  # 🔄 Refrescar la interfaz

# Título principal
st.title("🛒 Simulador de Abastecimiento en SAP")

st.write("Bienvenido/a al simulador de abastecimiento. Debes tomar decisiones correctas para completar el proceso con éxito.")

# ETAPA 1: Detección de la Necesidad
if st.session_state["etapa"] == 1:
    st.subheader("📌 Etapa 1: Detección de la Necesidad")
    st.write("Tu equipo necesita adquirir materiales para la oficina. ¿Qué tipo de bien o servicio necesitas?")

    if st.button("📄 Papelería"):
        avanzar(10, categoria="Papelería")  # Avanza con la categoría correcta

    if st.button("💻 Software"):
        avanzar(10, categoria="Software")  # Flujo especial para software

    if st.button("🛠️ Mantenimiento"):
        avanzar(10, categoria="Mantenimiento")  # Flujo especial para mantenimiento

# ETAPA 2: Carga de Solicitud (cambia según la elección)
elif st.session_state["etapa"] == 2:
    if st.session_state["categoria"] == "Papelería":
        st.subheader("📌 Etapa 2: Carga de Solicitud - Papelería")
        st.write("¿Dónde quieres cargar la solicitud de pedido?")
        if st.button("🖥️ SAP"):
            avanzar(10)
        if st.button("📋 Wrike"):
            avanzar(7)

    elif st.session_state["categoria"] == "Software":
        st.subheader("📌 Etapa 2: Carga de Solicitud - Software")
        st.write("El software requiere una Orden de Compra. ¿Cómo procederás?")
        if st.button("📝 Crear OC en SAP"):
            avanzar(10)
        if st.button("⚠️ No crear OC (incorrecto)"):
            avanzar(-5)

    elif st.session_state["categoria"] == "Mantenimiento":
        st.subheader("📌 Etapa 2: Carga de Solicitud - Mantenimiento")
        st.write("Antes de proceder con el mantenimiento, se necesita una aprobación.")
        if st.button("✅ Enviar solicitud de aprobación"):
            avanzar(10)
        if st.button("⚠️ Continuar sin aprobación (incorrecto)"):
            avanzar(-5)

# ETAPA 3: Selección del Proveedor (igual para todas las categorías)
elif st.session_state["etapa"] == 3:
    st.subheader("📌 Etapa 3: Selección del Proveedor")
    st.write("¿A qué proveedor eliges?")
    if st.button("✅ Proveedor Sugerido"):
        avanzar(10)
    if st.button("🆕 Nuevo Proveedor (no registrado)"):
        avanzar(-5)

# ETAPA 4: Recepción del Bien o Servicio
elif st.session_state["etapa"] == 4:
    st.subheader("📌 Etapa 4: Recepción del Bien o Servicio")
    st.write("El proveedor ha entregado el pedido. ¿Todo llegó correctamente?")
    if st.button("✔️ Sí, todo correcto"):
        avanzar(10)
    if st.button("❌ No, hay errores en la entrega"):
        avanzar(-5)

# ETAPA 5: Autorización del Gasto
elif st.session_state["etapa"] == 5:
    st.subheader("📌 Etapa 5: Autorización del Gasto")
    st.write("Debes autorizar el gasto. ¿Qué datos necesitas?")
    if st.button("📑 Orden de Compra, Importe, Fecha, Concepto"):
        avanzar(10)
    if st.button("📜 Solo Factura"):
        avanzar(-5)

# ETAPA 6: Pago al Proveedor
elif st.session_state["etapa"] == 6:
    st.subheader("📌 Etapa 6: Pago al Proveedor")
    st.write("El área de Administración ha procesado la factura y realizado el pago. ¡Misión cumplida!")

    st.write(f"Tu puntaje final es: **{st.session_state['puntaje']}** puntos")

    if st.session_state["puntaje"] >= 50:
        st.success("🎉 ¡Muy bien! Seguiste correctamente el proceso.")
    else:
        st.warning("⚠️ Revisa las mejores prácticas del proceso de abastecimiento para optimizar tiempos.")

    if st.button("🔄 Reiniciar Juego"):
        st.session_state["puntaje"] = 0
        st.session_state["etapa"] = 1
        st.session_state["categoria"] = None
        st.experimental_rerun()  # 🔄 Refrescar la interfaz



