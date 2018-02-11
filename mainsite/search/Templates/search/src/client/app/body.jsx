import React from 'react';
import ReactDOM from 'react-dom';

export class Body extends React.Component{
    constructor(props){
        super(props);
        console.log(this.props.subjectName);
        console.log(this.props.professor);
        console.log(this.props.university);
    }
    render(){
        console.log(this.props.subjectName);
        console.log(this.props.professor);
        console.log(this.props.university);
        return <h2> hello</h2>
    }
}    