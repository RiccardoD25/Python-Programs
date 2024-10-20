import tkinter as tk
from tkinter import messagebox

class ChessBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = tk.Canvas(self.root, width=512, height=512)
        self.board.pack()
        
        self.tiles = {}
        self.selected_piece = None
        self.create_board()
        self.setup_pieces()

    def create_board(self):
        # Create 8x8 chessboard
        color = 'white'
        for row in range(8):
            for col in range(8):
                x1 = col * 64
                y1 = row * 64
                x2 = x1 + 64
                y2 = y1 + 64
                self.tiles[(row, col)] = self.board.create_rectangle(x1, y1, x2, y2, fill=color)
                color = 'black' if color == 'white' else 'white'
            color = 'black' if color == 'white' else 'white'
    
    def setup_pieces(self):
        # Place chess pieces (we'll use simple letters to represent them)
        self.pieces = {}
        
        # White pieces
        for col, piece in enumerate(['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']):
            self.pieces[(0, col)] = self.board.create_text(col*64 + 32, 32, text=piece, font=("Arial", 32), fill="black")
            self.pieces[(1, col)] = self.board.create_text(col*64 + 32, 96, text='P', font=("Arial", 32), fill="black")
        
        # Black pieces
        for col, piece in enumerate(['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']):
            self.pieces[(7, col)] = self.board.create_text(col*64 + 32, 512-32, text=piece, font=("Arial", 32), fill="white")
            self.pieces[(6, col)] = self.board.create_text(col*64 + 32, 512-96, text='p', font=("Arial", 32), fill="white")
        
        # Bind the click events for piece movement
        self.board.bind("<Button-1>", self.on_click)
    
    def on_click(self, event):
        # Get the clicked square
        col = event.x // 64
        row = event.y // 64
        
        if self.selected_piece:
            # If a piece is selected, move it to the new square
            self.move_piece(row, col)
        else:
            # Select a piece
            self.select_piece(row, col)
    
    def select_piece(self, row, col):
        # Select the piece at the given row, col
        piece = self.pieces.get((row, col))
        if piece:
            self.selected_piece = (row, col)
            self.board.itemconfig(piece, fill="green")
    
    def move_piece(self, row, col):
        # Move the selected piece to the new square
        if (row, col) not in self.pieces:
            piece = self.pieces.pop(self.selected_piece)
            self.board.coords(piece, col*64 + 32, row*64 + 32)
            self.pieces[(row, col)] = piece
            self.board.itemconfig(piece, fill="black" if row < 2 else "white")
            self.selected_piece = None
        else:
            messagebox.showwarning("Invalid Move", "Square already occupied!")
            self.board.itemconfig(self.pieces[self.selected_piece], fill="black" if self.selected_piece[0] < 2 else "white")
            self.selected_piece = None

# Run the chess game
if __name__ == "__main__":
    root = tk.Tk()
    chess_game = ChessBoard(root)
    root.mainloop()
