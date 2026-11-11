import time, numpy as np, scipy, matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from utils import readInput

def loadInput(filename: str) -> np.ndarray:
    lines = readInput(filename)
    rolls = np.zeros(shape=(len(lines), len(lines[0]))).astype(np.uint8)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "@":
                rolls[y][x] = 1
    return rolls

kernel = np.ones((3, 3), dtype=np.uint8)
kernel[1, 1] = 0

def forklift(state):
    nb = scipy.signal.convolve2d(state, kernel, mode='same')
    state &= nb > 3
    return np.sum(state)

def part1(rolls: np.ndarray):
    init = np.sum(rolls)
    count = forklift(rolls)
    print (f"🎄 Part 1: {init-count}", end='')

def part2(rolls: np.ndarray):
    frames = []
    init = np.sum(rolls)
    frames.append(1-rolls)
    fig, ax = plt.subplots(figsize=(5, 5))
    im = ax.imshow(frames[0], cmap='gray', vmin=0, vmax=1) 
    ax.axis('off')

    prev = 0
    count = -1
    while count != prev:
        prev = count
        count = forklift(rolls)
        frames.append(1-rolls)

    def update(frame_number):
        im.set_array(frames[frame_number])
        return [im]

    anim = FuncAnimation(fig, update, frames=len(frames), interval=50, blit=True)
    anim.save('animazione_matrice.gif', writer='pillow', fps=20)
    print (f"🎄🎅 Part 2: {init-count}", end='')

if __name__ == "__main__":
    title = "Day 4: Printing Department"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_4.txt")
    
    t0 = time.perf_counter()
    part1(inputs)
    print (" - {:.5f}".format(time.perf_counter()-t0))
    
    t0 = time.perf_counter()
    part2(inputs)
    print (" - {:.5f}".format(time.perf_counter()-t0))
