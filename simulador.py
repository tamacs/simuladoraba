import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Simulador de Abastecimiento", layout="wide")

# Inicializar variables de sesión correctamente
if "puntaje" not in st.session_state:
    st.session_state["puntaje"] = 0
if "etapa" not in st.session_state:
    st.session_state["etapa"] = 1
if "error" not in st.session_state:
    st.session_state["error"] = False  # Para mostrar mensajes de error

# Función para avanzar de etapa
def avanzar(puntos, error=False):
    if error:
        st.session_state["error"] = True  # Activa el mensaje de error
    else:
        st.session_state["puntaje"] += puntos
        st.session_state["etapa"] += 1
        st.session_state["error"] = False  # Limpia errores previos
    st.experimental_rerun()  # 🔄 Refrescar la pantalla

# Título principal
st.title("🛒 Simulador de Abastecimiento en SAP")

st.write("Bienvenido/a al simulador de abastecimiento. Debes tomar decisiones correctas para completar el proceso con éxito.")

# Mostrar mensajes de error si hay
if st.session_state["error"]:
    st.error("❌ Error: Tomaste una decisión incorrecta. Revisa el proceso y vuelve a intentarlo.")

# ETAPA 1: Detección de la necesidad
if st.session_state["etapa"] == 1:
    st.subheader("📌 Etapa 1: Detección de la Necesidad")
    st.write("Tu equipo necesita adquirir materiales para la oficina. ¿Qué tipo de bien o servicio necesitas?")

    if st.button("📄 Papelería"):
        avanzar(10)
    if st.button("💻 Software"):
        avanzar(-5, error=True)  # ❌ Penalización y mensaje de error

# ETAPA 2: Carga de Solicitud
elif st.session_state["etapa"] == 2:
    st.subheader("📌 Etapa 2: Carga de Solicitud")
    st.write("¿Dónde quieres cargar la solicitud de pedido?")

    if st.button("🖥️ SAP"):
        avanzar(10)
    if st.button("📋 Wrike"):
        avanzar(7)
    if st.button("✖️ No cargar la solicitud"):
        avanzar(-10, error=True)  # ❌ Error, no se puede continuar sin solicitud

# ETAPA 3: Selección del Proveedor
elif st.session_state["etapa"] == 3:
    st.subheader("📌 Etapa 3: Selección del Proveedor")
    st.write("¿A qué proveedor eliges?")

    if st.button("✅ Proveedor Sugerido"):
        avanzar(10)
    if st.button("🆕 Nuevo Proveedor (no registrado)"):
        avanzar(-5, error=True)  # ❌ Penalización por retrasos en registro

# ETAPA 4: Recepción del Bien o Servicio
elif st.session_state["etapa"] == 4:
    st.subheader("📌 Etapa 4: Recepción del Bien o Servicio")
    st.write("El proveedor ha entregado el pedido. ¿Todo llegó correctamente?")

    if st.button("✔️ Sí, todo correcto"):
        avanzar(10)
    if st.button("❌ No, hay errores en la entrega"):
        avanzar(-5, error=True)  # ❌ Penalización por gestión de reclamos

# ETAPA 5: Autorización del Gasto
elif st.session_state["etapa"] == 5:
    st.subheader("📌 Etapa 5: Autorización del Gasto")
    st.write("Debes autorizar el gasto. ¿Qué datos necesitas?")

    if st.button("📑 Orden de Compra, Importe, Fecha, Concepto"):
        avanzar(10)
    if st.button("📜 Solo Factura"):
        avanzar(-5, error=True)  # ❌ Error, falta información

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
        st.session_state["error"] = False
        st.experimental_rerun()  # 🔄 Refrescar la interfaz


