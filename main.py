import kivy
kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import BooleanProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
import sys
from kivy.core.audio import SoundLoader


class TicTacToeGame(Widget):
	player_tracker = 0
	finished = BooleanProperty(False)
	game_checker = 0
	player1_won_already = False
	player2_won_already = False
	winner = ""
	player1_score = NumericProperty(0)
	player2_score = NumericProperty(0)
	board = {'00': '', '01': '', '02': '', '10': '', '11': '', '12': '', '20': '', '21': '', '22': ''}
	
	box = BoxLayout(orientation= "vertical", size_hint= (1, 1))
	grid = GridLayout(cols= 2, rows= 1, size_hint= (1, .4))
	
	ok_btn = Button(text= "Yes")
	cancel_btn = Button(text= "No")
	
	grid.add_widget(cancel_btn)
	grid.add_widget(ok_btn)
	
	box.add_widget(Label(text= "Are you sure you want to exit?", font_size= dp(17)))
	box.add_widget(grid)
	popup = Popup(title= "Quit", size_hint= (.8, .4), content= box, auto_dismiss= False, title_size= dp(20), separator_height= dp(5))
	
	cancel_btn.bind(on_release= popup.dismiss)
	ok_btn.bind(on_release= sys.exit)
	
	def flip(self, widget, idx):
		if widget.text == "":
			if self.player_tracker % 2 == 0:
				self.board[f"{idx}"] = "O"
				widget.text = "O"
				widget.color = (0, 0, 1, 1)
				self.ids.winner_label.text = "Player 2"
				
				winner = self.check_winner()
				
				if winner:
					self.ids.winner_label.text = "Player 1 Won!!!"
					self.win_music()
					self.finished = True
					self.player1_score += 1
					self.player1_won_already = True
					
				elif not winner and self.game_checker == 8:
					self.ids.winner_label.text = "It's a draw!!!"
					self.win_music()
					self.finished = True
				
			else:
				self.board[f"{idx}"] = "X"
				widget.text = "X"
				widget.color = (1, 0, 0,1)
				self.ids.winner_label.text = "Player 1"
				
				winner = self.check_winner()
				
				if winner:
					self.ids.winner_label.text = "Player 2 Won!!!"
					self.win_music()
					self.player2_score += 1
					self.finished = True
					self.player2_won_already = True
					
				elif not winner and self.game_checker == 8:
					self.ids.winner_label.text = "It's a draw!!!"
					self.win_music()
					self.finished = True
	
			self.player_tracker += 1
			self.game_checker += 1
			
	
	def win_music(self):
		self.win_sound = SoundLoader.load("assets/point.ogg")
		self.win_sound.volume = 0.2
		self.win_sound.play()
		
		
	def check_winner(self):
		# rows
		for i in range(3):
			if self.board[f"{i}0"] == self.board[f"{i}1"] and self.board[f"{i}0"] == self.board[f"{i}2"]:
				return self.board[f"{i}0"]
				
		# columns
		for i in range(3):
			if self.board[f"0{i}"] == self.board[f"1{i}"] and self.board[f"0{i}"] == self.board[f"2{i}"]:
				return self.board[f"0{i}"]
				
		# diagonals
		if self.board["00"] == self.board["11"] and self.board["00"] == self.board["22"]:
			return self.board["00"]
			
		if self.board["02"] == self.board["11"] and self.board["02"] == self.board["20"]:
			return self.board["02"]
	
		
	def restart_game(self):
		self.ids.c1r1.text = ""
		self.ids.c2r1.text = ""
		self.ids.c3r1.text = ""
		self.ids.c1r2.text = ""
		self.ids.c2r2.text = ""
		self.ids.c3r2.text = ""
		self.ids.c1r3.text = ""
		self.ids.c2r3.text = ""
		self.ids.c3r3.text = ""
		
		self.board = {'00': '','01': '','02': '','10': '','11': '','12': '','20': '','21': '','22': ''}
		self.finished = False
		self.game_checker = 0
		
	def quit_game(self):
		self.popup.open()


class TicTacToeApp(App):
	def build(self):
		Window.clearcolor = (104/255.0, 97/255.0, 50/255.0, 1)
		return TicTacToeGame()
		
		
if __name__ == "__main__":
	TicTacToeApp().run()