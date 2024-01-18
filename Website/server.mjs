import express from 'express'
import axios from 'axios'

var app = express()

app.set('view engine', 'ejs');
app.use(express.static('public'))
 
app.get('/extract/:url' , (req,res) =>
{
    console.log(req.params['url']);
})

app.use('/', (req,res) =>
{   
    res.render('index');
})


app.listen(3000, ()=>{
    console.log("Server is running on port 3000")
})