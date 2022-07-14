import streamlit as st
import pandas as pd 
from db_fxns import * 
import streamlit.components.v1 as stc



# Data Viz Pkgs
import plotly.express as px 


HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Pengisian Data OOH Djarum & Kompetitor</h1>
    <p style="color:white;text-align:center;">DSO Pamekasan</p>
    </div>
    """


def main():
	stc.html(HTML_BANNER)


	menu = ["Create","Read","Update","Delete","About"]
	choice = st.sidebar.selectbox("Menu",menu)
	create_table()

	if choice == "Create":
		st.subheader("Add Item")
		col1,col2 = st.columns(2)
		
		with col1:
			task = st.selectbox("Pabrikan",[
                     "--- Input Pabrikan ---",
                     "Djarum",
                     "GG",
                     "PMI",
                     "NTI"
                    ]
                    )

		with col2:
			task_status = st.selectbox("Jenis OOH",[
                        "--- Jenis OOH ---",
                        "Billboard - 10m x 5m",
                        "Billboard - 5m x 10m",
                        "Billboard - 8m x 4m",
                        "Billboard - 4m x 8m",
                        "Baliho - 6m x 4m",
                        "Midis - 3m x 6m",
                        "Midis - 4m x 2m",
                        "Midis - 2m x 4m",
                        "PJU - 2m x 1m"
                            ]
                        )
			task_due_date = st.text_area("Diisi Jenis Lampu-Jumlah Titik-Jumlah Muka-Alamat-Zona. (Contoh Pengisian : BL-1-1-Pemuda Kaffa-Bangkalan)")

		if st.button("Submit"):
			add_data(task,task_status,task_due_date)
			st.success("Terima Kasih Sudah Mengisi Form Dengan Benar".format(task))


	elif choice == "Read":
		# st.subheader("View Items")
		with st.expander("View All"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["Pabrikan","Jenis OOH","Alamat"])
			st.dataframe(clean_df)
                

    

####		with st.expander("Task Status"):
####			task_df = clean_df['Status'].value_counts().to_frame()
			# st.dataframe(task_df)
####			task_df = task_df.reset_index()
####			st.dataframe(task_df)

####			p1 = px.pie(task_df,names='index',values='Status')
####			st.plotly_chart(p1,use_container_width=True)


	elif choice == "Update":
		st.subheader("Edit Items")
		with st.expander("Current Data"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["Pabrikan","Jenis OOH","Alamat"])
			st.dataframe(clean_df)

		list_of_tasks = [i[0] for i in view_all_task_names()]
		selected_task = st.selectbox("Pabrikan",list_of_tasks)
		task_result = get_task(selected_task)
		# st.write(task_result)

		if task_result:
			task = task_result[0][0]
			task_status = task_result[0][1]
			task_due_date = task_result[0][2]

			col1,col2 = st.columns(2)
			
			with col1:
				new_task = st.text_area("Pabrikan",task)

			with col2:
				new_task_status = st.selectbox("Jenis OOH",[
                        "--- Jenis OOH ---",
                        "Billboard - 10m x 5m",
                        "Billboard - 5m x 10m",
                        "Billboard - 8m x 4m",
                        "Billboard - 4m x 8m",
                        "Baliho - 6m x 4m",
                        "Midis - 3m x 6m",
                        "Midis - 4m x 2m",
                        "Midis - 2m x 4m",
                        "PJU - 2m x 1m"
                            ]
                        )
				new_task_due_date = st.text_area("Alamat")

			if st.button("Update Task"):
				edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
				st.success("Updated ::{} ::To {}".format(task,new_task))

			with st.expander("View Updated Data"):
				result = view_all_data()
				# st.write(result)
				clean_df = pd.DataFrame(result,columns=["Pabrikan","Jenis OOH","Alamat"])
				st.dataframe(clean_df)


	elif choice == "Delete":
		st.subheader("Delete")
		with st.expander("View Data"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["Pabrikan","Jenis OOH","Alamat"])
			st.dataframe(clean_df)

		unique_list = [i[0] for i in view_all_task_names()]
		delete_by_task_name =  st.selectbox("Select Task",unique_list)
		if st.button("Delete"):
			delete_data(delete_by_task_name)
			st.warning("Deleted: '{}'".format(delete_by_task_name))

		with st.expander("Updated Data"):
			result = view_all_data()
			# st.write(result)
			clean_df = pd.DataFrame(result,columns=["Pabrikan","Jenis OOH","Alamat"])
			st.dataframe(clean_df)

	else:
		st.subheader("About ToDo List App")
		st.info("Built with Streamlit")
		st.info("Jesus Saves @JCharisTech")
		st.text("Jesse E.Agbe(JCharis)")


if __name__ == '__main__':
	main()
