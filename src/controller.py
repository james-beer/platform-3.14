class Controller:
    """Hardware controller."""

    def __init__(self, junctions):
        """Initializes the controller with a list of junctions. 
    
        Parameters:
        junctions - a list of tuples of the form ('junction_name', ['route_name', ...])
        """
        self.junctions = dict(junctions)
        self.selected_routes = dict([(junction, routes[0]) for junction, routes in zip(self.junctions.keys(), self.junctions.values())])

    def get_junctions(self):
        """Gets the junctions in the track layout."""
        return self.junctions.keys()

    def get_route(self, junction_name):
        """Gets the selected route for a junction."""
        return self.selected_routes[junction_name]

    def get_routes(self, junction_name):
        """Gets the list of routes for a junction."""
        return self.junctions[junction_name]

    def change_route(self, junction_name, route):
        """Changes the selected route for a junction."""
        print("{} set to {}".format(junction_name, route))
        self.selected_routes[junction_name] = route
        # to do: implement controller logic
