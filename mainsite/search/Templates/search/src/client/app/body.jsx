import React from 'react';
import ReactDOM from 'react-dom';

var subjectName1;
var professor1;
var university1;
var tags1;


function tag_expander(input_tag){
    var returnstring = input_tag[0];
    console.log(input_tag)
    for(var i=1; i<input_tag.length; i++){
        console.log(returnstring);
        returnstring = returnstring+", "+input_tag[i];
    }
    returnstring = returnstring+".";
    return returnstring;
}

function lister(count, results){
    console.log(results);
    subjectName1 =[];
    professor1=[];
    university1=[];
    tags1=[];
    for(var i=0; i<count; i++){
        console.log(i);
        subjectName1.push(results[i].subjectName);
        professor1.push(results[i].professor_name);
        university1.push(results[i].university);
        tags1.push(tag_expander(results[i].pdf_tags));
    }
    console.log(professor1);
}

export class Body extends React.Component{
   

    constructor(props){
        super(props);
        //console.log(this.props.subjectName);
        //console.log(this.props.professor);
        //console.log(this.props.university);
        
        this.state = {count:0};  
    }

    

    render(){
        if(this.props.json.count>0){
            lister(this.props.json.count, this.props.json.results);
            var lister_in_progress = subjectName1.map((item, index)=>{
                return (
                    <div class="card text-left mt-3">
                        <img class="card-img-top" src="holder.js/100px180/" alt="" />
                        <div class="card-body">
                            <h4 class="card-title">{item}</h4>
                            <p class="card-text">University: {university1[index]}</p>
                            <p class="card-text">Professor: {professor1[index]}</p>
                            <p class="card-text">Tags: {tags1[index]}</p>
                        </div>
                    </div>
                )
            });
            return <div class="container mt-5">
                {lister_in_progress}
            </div> 
    }
    return <div></div>
    }
}    