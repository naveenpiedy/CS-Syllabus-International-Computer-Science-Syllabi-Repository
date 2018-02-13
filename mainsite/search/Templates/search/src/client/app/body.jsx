import React from 'react';
import ReactDOM from 'react-dom';



export class Body extends React.Component{
    constructor(props){
        super(props);
        //console.log(this.props.subjectName);
        //console.log(this.props.professor);
        //console.log(this.props.university);
        
        this.state = {count:0};
        console.log("Yeahhhhhhhhh");   
    }
    render(){
        return <h2>{JSON.stringify(this.props.json)}</h2>
        console.log("die");
    }
}    