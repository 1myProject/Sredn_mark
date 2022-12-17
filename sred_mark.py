from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout



class vApp(App):
	
	def sr(self,ev):
	    sredn=sum(self.vse) / len(self.vse)
	    self.lbtx=''
	    self.vse=[]
	    self.lb.text=str(sredn)
	
	def clr(self,ev):
	    self.lbtx=''
	    self.vse=[]
	    self.upup()
	
	def delit(self,ev):
	    self.lbtx=self.lbtx[:len(self.lbtx)-3]
	    self.vse=self.vse[:len(self.vse)-1]
	    self.upup()
	
	def upup(self):
		self.lb.text=self.lbtx
	
	def build(self):
		
		self.f='{:3}'
		self.lbtx=""
		self.vse=[]
		
		bx=BoxLayout(orientation = 'vertical')
		self.lb=Label(text="")
		bx.add_widget(self.lb)
		
		gl=GridLayout(rows=4,cols=3)
		for i in range(10):
			gl.add_widget(Button(text=str(i+1),on_press=self.cl))
		bl=BoxLayout()
		bl.add_widget(Button(text='del',on_press=self.delit))
		bl.add_widget(Button(text='clr',on_press=self.clr))
		gl.add_widget(bl)
		gl.add_widget(Button(text='сред',on_press=self.sr))
		bx.add_widget(gl)
		return bx
		
	def cl(self,ev):
		self.vse.append(int(ev.text))
		self.lbtx+=self.f.format(ev.text)
		self.upup()
		
	
		
		
vApp().run()