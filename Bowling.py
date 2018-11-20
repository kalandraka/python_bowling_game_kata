class Game(object):

    def __init__(self):
        self.rolls = {}
        self.current_roll = 0

    def _is_spare(self, first_in_frame):
        return self.rolls[first_in_frame] + self.rolls[first_in_frame + 1] == 10

    def _is_strike(self, first_in_frame):
        return self.rolls[first_in_frame] == 10

    def _two_balls_in_frame(self, first_in_frame):
        return self.rolls[first_in_frame] + self.rolls[first_in_frame + 1]

    def _next_ball_for_spare(self, first_in_frame):
        return self.rolls[first_in_frame + 2]

    def _next_two_balls_for_strike(self, first_in_frame):
        return self.rolls[first_in_frame + 1] + self.rolls[first_in_frame + 2]

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def score(self):
        score_value = 0
        first_ball_in_frame = 0
        for frame in range(0, 10):
            if self._is_strike(first_ball_in_frame):
                score_value += 10 + self._next_two_balls_for_strike(first_ball_in_frame)
                first_ball_in_frame += 1
            elif self._is_spare(first_ball_in_frame):
                score_value += 10 + self._next_ball_for_spare(first_ball_in_frame)
                first_ball_in_frame += 2
            else:
                score_value += self._two_balls_in_frame(first_ball_in_frame)
                first_ball_in_frame += 2

        return score_value
