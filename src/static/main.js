const app = new Vue({
  el: '#app',
  data: {
    junctions: []
  },
  methods: {
    getBaseUrl: function (junction) {
      return `/api/junction/${junction}`;
    },

    refresh: async function () {
      try {
        const names = await axios.get('/api/junctions');
        const requests = names.data.map(async name => {
          const baseUrl = this.getBaseUrl(name);
          const selectedRoute = await axios.get(`${baseUrl}/route`);
          const routes = await axios.get(`${baseUrl}/routes`);
          return {
            name,
            routes: routes.data.map(route => {
              return {
                name: route,
                isSelected: route === selectedRoute.data
              };
            })
          };
        });
        this.junctions = await Promise.all(requests);
      } catch (error) {
        console.error(error);
      }
    },

    selectRoute: async function (junction, route) {
      try {
        const baseUrl = this.getBaseUrl(junction);
        await axios.post(`${baseUrl}/route`, { route: route });
        await this.refresh();
      } catch (error) {
        console.error(error);
      }
    }
  }
});

// Refresh the data now and then every 60s.
setInterval(app.refresh, 60000);
app.refresh();