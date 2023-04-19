import React, {useState, useEffect} from 'react' 
import axios from 'axios';


function App(){
  const [data, setData] = useState()

  useEffect(() =>{
    axios.get("/test")
      .then(response => {
        setData(response.data);
        console.log({"this is the first get axios request ":data})
      })
      .catch(error => {
        console.log(error);
      });
  }, [])
  return (
    <div>
      <p>hi!</p>
    </div>
  )
}

export default App
