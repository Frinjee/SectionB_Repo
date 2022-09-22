import customtkinter

class EntryFrame(customtkinter.CTkFrame):
	def __init__(self, *args, header_name='Input Frame', **kwargs):
		super().__init__(*args, **kwargs)
		
		self.header_name = header_name
		
		self.header = customtkinter.CTkLabel(self, text=self.header_name)
		self.header.grid(row=0, column=0, padx=10, pady=10)
		
		self.entry_input = customtkinter.StringVar(value='')
		
		# decimal to binary entry
		self.d2b_entry = customtkinter.CTkEntry(self, placeholder_text='Enter Decimal')
		self.d2b_entry.grid(row=1, column=0, padx=10, pady=10)
		
		# decimal to octal entry
		self.d2o_entry = customtkinter.CTkEntry(self, placeholder_text='Enter Decimal')
		self.d2o_entry.grid(row=2, column=0, padx=10, pady=10)
		
		# decimal to base entry
		self.d2base_entry = customtkinter.CTkEntry(self, placeholder_text='Enter Decimal')
		self.d2base_entry.grid(row=3, column=0, padx=10, pady=10)
		
		# base to decimal entry
		self.b2d_entry = customtkinter.CTkEntry(self, placeholder_text='Select Base & Enter Decimal')
		self.b2d_entry.grid(row=4, column=0, padx=10, pady=10)
	
	def get_value(self):
		return self.entry_input.get()
	
	def set_value(self):
		self.entry_input.set()

