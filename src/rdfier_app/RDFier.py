import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image
from unco import UNCO_PATH
from unco.data.rdf_data import RDFData
from unco.features.illustrator import Illustrator
from unco.features.graph_generator import GraphGenerator

st.set_page_config(
    page_title="RDFier",
    layout="wide")

def update():
    st.session_state.rdf_data = RDFData(st.session_state.df.copy())

def activate_rerun():
    st.session_state.rerun = True

# Begin webpage---------------------------------------------------------------------------

st.title('RDFier')
st.subheader("A RDF Mapper")

button1, button2 = st.columns(2)

uploaded_file = button1.file_uploader("Upload", type=["csv"], accept_multiple_files=False)

uploaded_prefixes = button2.file_uploader("Prefixes", type=["csv"], accept_multiple_files=False)

if not uploaded_file:
    st.session_state.df = None
    st.session_state.generate = False
    st.session_state.rdf_data = None
    st.session_state.rerun = True
else:
    st.session_state.df = st.data_editor(pd.read_csv(uploaded_file), on_change=activate_rerun)
    if st.session_state.rerun:
        update()

    with st.container():
        col1, col2 = st.columns(2)

        turtle_format = col1.radio("RDF Format", ("Turtle", "XML"), on_change=activate_rerun)

        graphical_version = col2.checkbox("Show graph figure", value=True)

        solution = col2.selectbox("Select model:", (1,2,3,4,5,6,7,8,"9a","9b"), on_change=activate_rerun)
        if solution=="9a":
            solution = 9
            graphical_version = False
            turtle_format = "Turtle"
        elif solution=="9b":
            solution = 10
            graphical_version = False
            turtle_format = "Turtle"
    # Graph generieren-------------------------------------------------------------------------------

    generate = st.button("Generate RDF graph")

    if generate:
        st.session_state.generate = True
        st.session_state.rerun = True

    if st.session_state.generate:
        if st.session_state.rerun:
            st.session_state.rerun = False
            generator = GraphGenerator(st.session_state.rdf_data)
            if uploaded_prefixes: generator.load_prefixes(pd.read_csv(uploaded_prefixes))
            generator.generate_graph(model_id=solution,xml_format=(turtle_format=="XML"))

        
        path = Path(UNCO_PATH, "data/output/graph" + (".ttl" if turtle_format=="Turtle" else ".rdf"))

        if generator.rdfdata.data.shape[0] > 30:
            graphical_version = False
            st.warning("RDF Graph is to large to generate figure. Only inputs with <30 rows are currently showable.", icon="⚠️")

        if graphical_version:
            codcol, graphcol = st.columns(2)

            codcol.code(path.read_text(),language="turtle" if turtle_format=="Turtle" else "xml")

            grapher = Illustrator(path)
            
            image = Image.open(str(Path(UNCO_PATH, "data/output/downloaded_graph.png")))

            graphcol.image(image, output_format="PNG", use_column_width="auto")
        else:
            st.code(path.read_text(),language="turtle" if turtle_format=="Turtle" else "xml")

        if solution==9 or solution==10:
            st.warning("For RDF*, only the graphs in Turtle format can be output so far!", icon="⚠️")