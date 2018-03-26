import React from 'react';
import ReactDOM from 'react-dom';
import {Body} from './body.jsx';
import {BrowserRouter as Router, Redirect} from 'react-router-dom';

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    console.log("Yeah");
    return xmlHttp.responseText;
}

class App extends React.Component {


    constructor(props){
        super(props);
        this.state = {json:"", subjectName:""};
        this.sendProps = this.sendProps.bind(this);
    }

    sendProps(){
        let subjectName = document.getElementById("subjectName").value;
        let url = "http://127.0.0.1:8000/search/rest/?search="+subjectName+"&format=json";
        console.log(url);  
        let json = JSON.parse(httpGet(url));

        this.setState({json:json, subjectName:subjectName})
    }

  render () {
    return <Router>
    <span>
    <Redirect push to={"/search/searching#" +this.state.subjectName} />
    <div class="container mt-5 w-75 text-left ">
          <div class="row">
              <div class="col-md-9">
                  <div class="form-group">
                    <label for="subjectName" class="form-inline" >Enter the subject name to search</label>
                    <input type="text" class="form-control form-inline" name="subjectName" id="subjectName" aria-describedby="helpId" placeholder="" />
                    <small id="helpId" class="form-text form-inline text-muted">Enter your search terms</small>
                  </div>
              </div>
              <div class="col-md-3 align-self-center">
                  <button type="button" class="btn btn-dark" onClick={this.sendProps}>Search</button>
              </div>
          </div>
          <div>
          </div>
          
      </div>
      <Body json={this.state.json}/> 
    </span>  
    </Router>  
  }
}

ReactDOM.render(<App />, document.getElementById('app'));