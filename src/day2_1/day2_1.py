from sys import argv
from dataclasses import dataclass
from typing import Match

@dataclass
class Sub:
    depth: int = 0
    h_pos: int = 0

    def forward(this, n):
        this.h_pos += n
        return this.h_pos

    def down(this, n):
        this.depth += n
        return this.depth

    def up(this, n):
        this.depth -= n
        return this.depth

    def print_result(this):
        print(this.depth*this.h_pos)
        return
    
    def __repr__(this):
        return f"Sub:\n\tdepth: {sub.depth}\n\thorizontal position: {sub.h_pos}"
    def __str__(self) -> str:
        return f"Sub:\n\tdepth: {sub.depth}\n\thorizontal position: {sub.h_pos}"


with open(argv[len(argv)-1]) as fp : 
    entrada = list(map(lambda x: x.split(" "), fp.read().splitlines()))
    sub = Sub()
    # print(entrada)
    for inst in entrada:
        match inst:
            case ["forward", n]:
                sub.forward(int(n))
                # print(f"forward {n} adds {n} to your horizontal position, a total of {sub.h_pos}")
            case ["down", n]:
                sub.down(int(n))
                # print(f"down {n} adds {n} to your depth, resulting in a value of {sub.depth}") 
            case ["up", n]:
                sub.up(int(n))
                # print(f"up {n} decreases {n} to your depth, resulting in a value of {sub.depth}") 

    sub.print_result()