import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Simulador de Abastecimiento", layout="wide")

# Inicializar variables de sesión de manera segura
session_defaults = {
    "puntaje": 0,
    "etapa": 1,
    "categoria": None,
    "error_entrega": False,
    "error_visual": False,
    "monto_compra": None,
    "proveedor_nuevo": False,
}

for key, value in session_defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Función para avanzar de etapa con control de errores
def avanzar(puntos, categoria=None, error_entrega=False, error_visual=False, monto_compra=None, proveedor_nuevo=False):
    if categoria:
        st.session_state["categoria"] = categoria
    if monto_compra is not None:
        st.session_state["monto_compra"] = monto_compra
    if proveedor_nuevo:
        st.session_state["proveedor_nuevo"] = True
    if error_entrega:
        st.session_state["error_entrega"] = True
    if error_visual:
        st.session_state["error_visual"] = True
    else:
        st.session_state["puntaje"] += puntos
        st.session_state["etapa"] += 1
        st.session_state["error_visual"] = False
    st.experimental_rerun()

# Título principal
st.title("🛒 Simulador de Abastecimiento en SAP")
st.write("Simula el proceso de abastecimiento, tomando decisiones correctas.")

# Si hay error visual, mostrar mensaje de error
if st.session_state["error_visual"]:
    st.error("❌ Error en el procedimiento de abastecimiento.")

# Etapas del proceso
if st.session_state["etapa"] == 1:
    st.subheader("📌 Etapa 1: Detección de la Necesidad")
    st.write("¿Qué tipo de bien o servicio necesitas adquirir?")

    if st.button("📄 Papelería"):
        avanzar(10, categoria="Papelería")
    if st.button("💻 Software"):
        avanzar(10, categoria="Software")
    if st.button("🛠️ Mantenimiento"):
        avanzar(10, categoria="Mantenimiento")
    if st.button("🌍 Servicio Exterior"):
        avanzar(10, categoria="Servicio Exterior")

elif st.session_state["etapa"] == 2:
    st.subheader("📌 Etapa 2: Carga de Solicitud")
    monto = st.number_input("Ingresa el monto de la compra (sin IVA, en USD):", min_value=0.0, step=10.0)

    if st.button("Continuar"):
        if monto > 2000:
            st.warning("💰 Las compras mayores a U$S 2,000 requieren Orden de Compra.")
        avanzar(0, monto_compra=monto)

elif st.session_state["etapa"] == 3:
    st.subheader("📌 Etapa 3: Selección del Proveedor")
    st.write("Elige el proveedor:")

    if st.button("✅ Proveedor Sugerido"):
        avanzar(10)
    if st.button("🆕 Nuevo Proveedor"):
        avanzar(-5, proveedor_nuevo=True, error_visual=True)

elif st.session_state["etapa"] == 4:
    st.subheader("📌 Etapa 4: Recepción del Bien o Servicio")
    if st.button("✔️ Sí, todo correcto"):
        avanzar(10)
    if st.button("❌ No, hay errores en la entrega"):
        st.error("❌ Debes gestionar la corrección del pedido.")
        avanzar(-5, error_entrega=True, error_visual=True)

elif st.session_state["etapa"] == 5 and not st.session_state["error_entrega"]:
    st.subheader("📌 Etapa 5: Autorización del Gasto")
    if st.button("📑 Orden de Compra, Importe, Fecha, Concepto"):
        avanzar(10)
    if st.button("📜 Solo Factura"):
        st.error("❌ Faltan datos para autorizar el gasto.")
        avanzar(-5, error_visual=True)

elif st.session_state["etapa"] == 6 and not st.session_state["error_entrega"]:
    st.subheader("📌 Etapa 6: Pago al Proveedor")
    st.write(f"Tu puntaje final es: **{st.session_state['puntaje']}** puntos")

    if st.session_state["puntaje"] >= 50:
        st.success("🎉 ¡Muy bien! Seguiste correctamente el proceso.")
    else:
        st.warning("⚠️ Revisa las mejores prácticas del proceso de abastecimiento.")

    st.subheader("📢 Información Importante:")
    st.info("📅 **Las facturas se registran con una semana de retraso.**")
    st.info("💰 Para consultar fechas de pago, comunícate con el área de **Pagos**.")

    if st.button("🔄 Reiniciar Juego"):
        st.session_state.clear()
        st.experimental_rerun()

elif st.session_state["error_entrega"]:
    st.subheader("🚨 Proceso Interrumpido")
    st.error("❌ Error en la entrega. Debes corregirlo antes de continuar.")

    if st.button("🔄 Reiniciar Juego"):
        st.session_state.clear()
        st.experimental_rerun()











