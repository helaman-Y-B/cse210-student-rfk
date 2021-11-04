from game.action import Action


class DrawActorsAction():
    """Draw the actors(robot, artifacts) and also draw the actions(movement and placement).

    Steriotype:
        Responsive for the visual.

    Attributes:
        self.output: An instance of DrawActorsAction."""

    def __init__(self, output_service):
        """The constructor function."""
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.clear_screen()

        for i in cast.values():
            self._output_service.draw_actors(i)
        self._output_service.flush_buffer()
