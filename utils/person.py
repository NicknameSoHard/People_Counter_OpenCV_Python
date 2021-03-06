class Person:
    def __init__(self, xi, yi):
        self.x = xi
        self.y = yi
        self.tracks = []
        self.done = False
        self.state = 0
        self.dir = None

    def update_coords(self, xn, yn):
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn

    def timed_out(self):
        return self.done

    # Check state and cross line
    def going_up(self, mid_end):
        if len(self.tracks) >= 2:
            if not self.state:
                if (self.tracks[-1][1] < mid_end) and (self.tracks[-2][1] >= mid_end):
                    self.state = 1
                    self.dir = 'up'
                    return True
        return False

    def going_down(self, mid_start):
        if len(self.tracks) >= 2:
            if not self.state:
                if (self.tracks[-1][1] > mid_start) and (self.tracks[-2][1] <= mid_start):
                    self.state = 1
                    self.dir = 'down'
                    return True
        return False
