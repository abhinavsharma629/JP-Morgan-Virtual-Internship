import React, { Component } from 'react';
import DataStreamer, { ServerRespond } from './DataStreamer';
import Graph from './Graph';
import './App.css';

/**
 * State declaration for <App />
 */
interface IState {
  data: ServerRespond[],
  showGraph: boolean,
}

/**
 * The parent element of the react app.
 * It renders title, button and Graph react element.
 */
class App extends Component<{}, IState> {
  constructor(props: {}) {
    super(props);

    this.state = {
      // data saves the server responds.
      // We use this state to parse data down to the child element (Graph) as element property
      data: [],
      showGraph:false,
    };
  }


  /**
   * Render Graph react component with state.data parse as property data if showGraph is set to true
   else it returns a null element
   */
  renderGraph() {
    return this.state.showGraph? (<Graph data={this.state.data}/>) : null;
  }

  /**
   * Get new data from server and update the state with the new data
   */

  getUpdateDataFromServer() {
     DataStreamer.getData((serverResponds: ServerRespond[]) => {
       // Update the state by creating a new array of data that consists of
       // Previous data in the state and the new data from server
       this.setState({ showGraph:true, data: [...this.state.data, ...serverResponds] });
     });
  }

  // sets an interval for retrieving data every 100 ms
  getDataFromServer() {
    setInterval(()=>{
      this.getUpdateDataFromServer()
    },100)

  }

  /**
   * Render the App react component
   */
  render() {
    return (
      <div className="App">
        <header className="App-header">
          Bank & Merge Co Task 2
        </header>
        <div className="App-content">
          `{<button className="btn btn-primary Stream-button"
            // when button is click, our react app tries to request
            // new data from the server.
            // As part of your task, update the getDataFromServer() function
            // to keep requesting the data every 100ms until the app is closed
            // or the server does not return anymore data.
            onClick={() => {this.getDataFromServer()}}>
            Start Streaming Data
          </button>}`
          <div className="Graph">
            {this.renderGraph()}
          </div>:

        </div>
      </div>
    )
  }
}

export default App;