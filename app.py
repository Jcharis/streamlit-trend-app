import streamlit as st
import streamlit.components.v1 as stc  

# EDA pkg
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use('Agg')
import plotly.express as px 
from PIL import Image
import os

@st.cache
def load_image(img):
	im = Image.open(os.path.join(img))
	return im

LANG = {"python_lang":"Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects",
"julia_lang":"Julia is a high-level, high-performance, dynamic programming language. While it is a general purpose language and can be used to write any application, many of its features are well-suited for numerical analysis and computational science.Distinctive aspects of Julia's design include a type system with parametric polymorphism in a dynamic programming language; with multiple dispatch as its core programming paradigm. ",
"javascript_lang":"""JavaScript  often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.
Alongside HTML and CSS, JavaScript is one of the core technologies of the World Wide Web. JavaScript enables interactive web pages and is an essential part of web applications. The vast majority of websites use it for client-side page behavior, and all major web browsers have a dedicated JavaScript engine to execute it.""",
"r_lang":"R is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing. The R language is widely used among statisticians and data miners for developing statistical software and data analysis",
"go_lang":"Go is a statically typed, compiled programming language designed at Google by Robert Griesemer, Rob Pike, and Ken Thompson. Go is syntactically similar to C, but with memory safety, garbage collection, structural typing,[6] and CSP-style concurrency.The language is often referred to as Golang because of its domain name, golang.org, but the proper name is Go.",
"rust_lang":"Rust is a multi-paradigm programming language focused on performance and safety, especially safe concurrency. Rust is syntactically similar to C++, but can guarantee memory safety by using a borrow checker to validate references. Unlike other safe programming languages, Rust does not use garbage collection.",
"java_lang":"Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let application developers write once, run anywhere (WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation",
"c_lang":"C  is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, with a static type system. By design, C provides constructs that map efficiently to typical machine instructions. It has found lasting use in applications previously coded in assembly language. Such applications include operating systems and various application software for computer architectures that range from supercomputers to PLCs and embedded systems."}

html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:{};text-align:center;">Programming Languages Trend App </h1>
		</div>
		"""


def main():
	
	menu = ["Home","Trends","About"]
	choice = st.sidebar.selectbox("Menu",menu)


	st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)

	if choice == "Home":
		st.image(load_image('data/imgs/different-programming-languages.png'))
		
		info_col1,info_col2 = st.beta_columns(2)

		with info_col1:
			with st.beta_expander('Python'):
				st.write(LANG['python_lang'])

			with st.beta_expander('Julia'):
				st.write(LANG['julia_lang'])

			with st.beta_expander('R-Lang'):
				st.write(LANG['r_lang'])


		with info_col2:
			with st.beta_expander('Javascript'):
				st.write(LANG['javascript_lang'])

			with st.beta_expander('Go'):
				st.write(LANG['go_lang'])

			with st.beta_expander('C'):
				st.write(LANG['c_lang'])


	elif choice == 'Trends':
		# Plots
		df = pd.read_csv("data/clean_with_dates.csv",parse_dates=['Week'],index_col=['Week'])
		# st.dataframe(df)

		# All Columns
		all_columns = df.columns.tolist()
		lang_choices = st.multiselect("Choose Language",all_columns)
		new_df = df[lang_choices]

		col1,col2 = st.beta_columns(2)
		with st.beta_expander("Line Chart"):
			# Line Chart
			st.line_chart(new_df)
		with st.beta_expander("Area Chart"):
			# new_df2 = df[lang_choices]
			st.area_chart(new_df)

		with st.beta_expander("Pie Chart"):
			sum_df = pd.read_csv("data/lang_sum_num_data.csv")
			fig = px.pie(sum_df, values='Sum', names='lang', title='Population of European continent')
			st.plotly_chart(fig)

		# All Columns
		all_columns = df.columns.tolist()
		lang_choices = st.multiselect("Choose Program Language",all_columns,default=["Python"])
		year_interval = st.selectbox("Select Year",["2015","2016","2017","2018","2019","2020","All"])
		if year_interval == "All":
			ts = df 
		else:
			ts = df[year_interval]
		
		# Using Plotly
		fig = px.line(ts,x=ts.index,y=lang_choices)
		st.plotly_chart(fig,use_container_width=True)


if __name__ == '__main__':
	main()