import { IonButton, IonCol, IonContent, IonGrid, IonHeader, IonPage, IonRow, IonTitle, IonToolbar } from '@ionic/react';
import ExploreContainer from '../components/ExploreContainer';
import './Home.css';
import { useEffect, useState } from 'react';

const API = "/api"
const Home: React.FC = () => {
  const [imageUrl, setImageUrl] = useState("")
  useEffect(()=>{
    fetch(`${API}/get_image_url`).then(x=>x.json()).then((x)=>{
      if(x=="finished")
      {
        alert("You finished all of them!")
        return
      }
      setImageUrl(`${x[0]}`)
    })
  }, [])
  const submit = (e: any)=>{
    console.log(e.target.id)
    fetch(`${API}/submit?filename=${imageUrl}&decision=${e.target.id}`, {"method":"post"}).then(()=>{
      fetch(`${API}/get_image_url`).then(x=>x.json()).then((x)=>{
        if(x=="finished")
        {
          alert("You finished all of them!")
          return
        }
        setImageUrl(`${x[0]}`)
      })
    })
  }
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Image Cleaning</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <img style={{ width: "50%"}} src={`${API}/img?filename=${imageUrl}`}></img>
        <img style={{ width: "50%"}} src={`https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=${imageUrl.split("_")[0]}&t=l`}></img>
        <IonGrid>
          <IonRow>
            <IonCol size="6">
              <IonButton style={{ width: "100%" }} color="danger" id="false" onClick={submit}>No</IonButton>
            </IonCol>
            <IonCol size="6">
              <IonButton style={{ width: "100%" }} color="success" id="true" onClick={submit}>Yes</IonButton>
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
};

export default Home;
