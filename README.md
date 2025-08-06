# 🎮 Tetris Game

A classic implementation of the beloved puzzle game Tetris, built from scratch using Python and Pygame. Experience the timeless gameplay that has captivated players for decades with smooth controls, authentic mechanics, and progressive difficulty.

## 🌟 Features

### Core Gameplay
- **7 Classic Tetrominoes**: All original piece shapes (I, O, T, S, Z, J, L) with authentic colors
- **Smooth Movement**: Responsive controls with support for both arrow keys and WASD
- **Piece Rotation**: Full 360-degree rotation system with collision detection
- **Line Clearing**: Automatic detection and clearing of completed rows
- **Ghost Piece Effect**: Visual preview of where pieces will land (via hard drop)

### Game Mechanics
- **Progressive Difficulty**: Speed increases every 10 lines cleared
- **Scoring System**: 
  - 100 points per line cleared × current level
  - Bonus points for hard drops
  - Level-based multipliers
- **Next Piece Preview**: See what's coming next to plan your strategy
- **Collision Detection**: Precise boundary and piece overlap detection

### Visual & Audio
- **Clean Interface**: Minimalist design focusing on gameplay
- **Color-Coded Pieces**: Each tetromino type has its distinctive color
- **Real-time Stats**: Live tracking of score, level, and lines cleared
- **Game Over Screen**: Clear indication when game ends with restart option

## 🎯 Controls

| Action | Keys | Description |
|--------|------|-------------|
| **Move Left** | ←, A | Move piece left |
| **Move Right** | →, D | Move piece right |
| **Soft Drop** | ↓, S | Increase fall speed |
| **Rotate** | ↑, W | Rotate piece clockwise |
| **Hard Drop** | Space | Instantly drop piece |
| **Restart** | R | Start new game (when game over) |

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Pygame library

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/tetris-game.git
   cd tetris-game
   ```

2. **Install dependencies:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python tetris.py
   ```

## 🎪 How to Play

1. **Objective**: Clear horizontal lines by completely filling them with blocks
2. **Gameplay**: Tetrominoes fall from the top - move and rotate them to fit
3. **Line Clearing**: When a row is completely filled, it disappears and you score points
4. **Progression**: Game speed increases as you advance through levels
5. **Game Over**: When pieces reach the top of the playing field

### Scoring Strategy
- Clear multiple lines simultaneously for higher scores
- Use hard drops strategically for bonus points
- Plan ahead using the next piece preview
- Build up the sides and clear the middle for better line setups

## 🏗️ Technical Details

### Architecture
- **Object-Oriented Design**: Clean separation between game logic, pieces, and rendering
- **Modular Structure**: Easy to extend and modify
- **Efficient Collision Detection**: Optimized algorithms for smooth gameplay
- **State Management**: Proper handling of game states and transitions

### Code Structure
```
tetris.py
├── Tetromino Class      # Individual piece logic
├── TetrisGame Class     # Core game mechanics
├── Rendering Functions  # Display and UI
└── Main Game Loop      # Event handling and updates
```

## 🎨 Customization

The game is designed to be easily customizable:

- **Colors**: Modify the `TETROMINO_COLORS` dictionary
- **Speed**: Adjust `fall_speed` calculation for different difficulty curves
- **Grid Size**: Change `GRID_WIDTH` and `GRID_HEIGHT` constants
- **Scoring**: Modify scoring logic in the `clear_lines()` method
- **Controls**: Remap keys in the event handling section

## 🐛 Known Issues & Future Enhancements

### Potential Improvements
- [ ] Add sound effects and background music
- [ ] Implement hold piece functionality
- [ ] Add ghost piece visual preview
- [ ] Include pause/resume functionality
- [ ] Save high scores locally
- [ ] Add different game modes (Marathon, Sprint, etc.)
- [ ] Implement T-spin detection and scoring
- [ ] Add particle effects for line clears

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report Bugs**: Open an issue with detailed reproduction steps
2. **Suggest Features**: Propose new functionality or improvements
3. **Submit Pull Requests**: Fix bugs or implement new features
4. **Improve Documentation**: Help make the code more understandable

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by the original Tetris created by Alexey Pajitnov
- Built with the excellent Pygame library
- Thanks to the Python community for continuous support and resources



---

**Enjoy playing Tetris and happy coding! 🎮✨**
