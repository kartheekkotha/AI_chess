## OPTIMIZATION STATERGIES OF OUR AI 
- Evaluation statergies think of any other good statergies
    In order to traverse the search tree as above, the AI needs to know how to evaluate the
    board at any position to decide if white or black has the advantage. My evaluation
    function currently looks at three main things when evaluating the board:
       a) Material for white and black. Each piece has a value and the more pieces you have,
           the better off your position is likely to be. For example, if white has an extra
           queen, it has an advantage over black.
       b) Piece-square table values - for each piece, there is a table that stores the best
           squares that the particular piece should occupy. So if white has a knight at a
           good square that controls the centre of the board, whereas black has a knight
           at the corner of the board, the situation is evaluated as being more favourable
           for white.
       c) Reduction in points for doubled pawns, isolated pawns, and blocked pawns. If any
           side has a set of pawns with the above features their points are slightly lower
           to indicate a slight disadvantage in such a position.
       d) A checkmate: a position where this has occured gets a very high point, so that the
           AI moves towards this if it can. (or avoids it).
- Opening table played by grandmasters

--- 

## CODE STRUCTURE ALTERNATE PLANNING
- Include the present state in the state and then use the same function in play and everywhere
- so when we find the child nodes we can call play from the state maybe 