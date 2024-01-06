# Modified-Checkers-Game
This is a modified version of the classic checkers game created for academic purposes as a project for the AI Laboratory. The game introduces unique features, including vertical piece movements , special power pieces such as archers, king, and hero. The AI is implemented using the Min-Max algorithm with a depth level of 3 for strategic gameplay.

## Table of Contents

- [Features](#features)
- [AI Strategy](#ai-strategy)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to play](#how-to-play)
  - [Board Setup ](#board-setup)
  - [Valid Moves](#valid-moves)
  - [Special Piece Conversion](#special-piece-conversion)
  - [Strategy](#strategy)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Features
- **Modified Gameplay:** vertical piece movements instead of diagonal.
- **Special Power Pieces:**
  - **Archers:** Unique movement capabilities.
  - **King:** Special privileges and strategic advantages.
  - **Hero:** A powerful piece with enhanced abilities.
- **AI Opponent:** Implements Min-Max algorithm for intelligent decision-making.
- **Depth Level 3:** Balances between strategic thinking and computational efficiency.

## AI Strategy

The AI opponent in this game employs the Min-Max algorithm with a depth level of 3. This ensures strategic decision-making while maintaining computational efficiency. The algorithm explores possible moves up to three levels deep to determine the best move based on the current state of the board.


## Requirements
<ol>
  <li><b>Python 3.9.12 </b></li>
  <li><b>Pygame 2.3.0</b></li>
</ol>

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/abrarhasan3/Modified-Checkers-Game.git
2. Run **Checkers>Main.py** and play the game.   

## How to play
As this is a two player game, there two color of pieces. 
<ol>
  <li><b>White (AI)</b></li>
  <li><b>Black (Human)</b></li>
</ol>

There are Four type of pieces in this game. <br>


<table>
  <tr>
    <td colspan="2" align = "center">1. Soldier Piece </td>
    <td colspan="2" align = "center">2. Archer Pieces </td>
  </tr>
  <tr> 
  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture2.png" height = "200px" width="200px"/></td>
  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture7.png" height = "200px" width="200px"/></td>

  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture1.png" height = "200px" width="200px"/></td>
  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture5.png" height = "200px" width="200px"/></td>
 
  </tr>
  <tr>
    <td colspan="2" align = "center">3. King Pieces </td>
    <td colspan="2" align = "center">4. Hero Pieces </td>
  </tr>
  <tr> 
  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture3.png" height = "200px" width="200px"/></td>
  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture6.png" height = "200px" width="200px"/></td>

  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture4.png" height = "200px" width="200px"/></td>
  <td><img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture8.png" height = "200px" width="200px"/></td>
 
  </tr>
  </table>
  
### Board Setup 
The board has 8 piece in each team. Among them 2 are archers. 
<img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture9.png" align="center" height="600px" width="600px"/>

### Valid Moves
|||
|---|:---:|
|**1. Soldier piece can move front vertically. It can not move back.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/soilder_move.png" height = "100px" width ="100px">|
|**2. Archer piece can move front vertically or diagonally. It can not move back**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/Archer%20Piece.png" height = "100px" width ="100px">|
|**3. King piece can move front vertically or diagonally and it can come back one cell.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/King_move.png" height = "100px" width ="100px">|
|**4. Hero piece can move front and bach in both vertically or diagonally.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/Hero_move.png" height = "100px" width ="100px">

### Special Piece Conversion
|||
|---|:---:|
|**1. If the soldier piece can reach the other end of the board it becomes a king.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/king_convert.png" height = "150px" width ="250px">|
|**2. When the Archer piece reaches the other end of the board it becomes a hero.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/hero_convert.png" height = "150px" width ="250px">|
### Strategy
|||
|---|:---:|
|**1.Solder piece can vertically jump over the opponent piece and capture them.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/Soldier%20Capture.gif" height = "250px" width ="250px">|
|**2. Archer piece can capture diagonally or vertically in front.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/Archer%20Capture.gif" height = "250px" width ="250px">|
|**3. King piece can capture diagonally or vertically in front or one box behing.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/King%20Piece.gif" height = "250px" width ="250px">|
|**4. Hero piece can capture diagonally or vertically in front or back direction.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/Hero%20Piece%20Capture.gif" height = "150px" width ="250px">|
|**5. Two opponent pieces can be captured at one move if double hop is possible.**|<img src="https://github.com/abrarhasan3/Modified-Checkers-Game/blob/main/img/Double%20Hop.gif" height = "150px" width ="250px">|
## Screenshots

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the game.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for academic and educational purposes.


## Authors

- [Abrar Hasan](https://www.github.com/abrarhasan3)

- [Nishat Sadaf Lira](https://github.com/Lira1999)
