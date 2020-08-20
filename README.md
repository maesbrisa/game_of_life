# game_of_life

![pytest](https://github.com/maesbrisa/game_of_life/workflows/CI/badge.svg)

## Requirements
1. Any live cell with less than 2 live neighbors dies (under population)
2. Any live cell with 2 or 3 live neighbors lives (next generation)
3. Any live cell with +3 live neighbors dies (over population)
4. Any dead cell with 3 live neighbors becomes live cell (reproduction)

## Example
```
stage_0 = [[0,1,1],[0,0,1],[0,0,0]]
stage_1 = [[0,0,1],[0,0,0],[0,0,0]]
```