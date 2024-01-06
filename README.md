# Modified-Checkers-Game
This is a modified version of the classic checkers game created for academic purposes as a project for the AI Laboratory. The game introduces unique features, including horizontal piece movements , special power pieces such as archers, king, and hero. The AI is implemented using the Min-Max algorithm with a depth level of 3 for strategic gameplay.

## Table of Contents

- [Features](#features)
- [Game Rules](#game-rules)
- [AI Strategy](#ai-strategy)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Features

- **Modified Gameplay:** Horizontal piece movements instead of diagonal.
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

## How to play
As this is a two player game, there two color of pieces. 
<ol>
  <li><b>White (AI)</b></li>
  <li><b>Black (Human)</b></li>
</ol>

There are Four type of pieces in this game. 


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
  
  ### Game Play 
The board has 8 piece in each, where there is 2 pieces in 
<img src = "https://github.com/abrarhasan3/Modified-Checkers-Game/blob/abrar/img/Picture9.png" align="center" height="600px" width="600px"/>

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
