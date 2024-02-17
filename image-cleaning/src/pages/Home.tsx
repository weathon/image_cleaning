import { IonButton, IonCol, IonContent, IonGrid, IonHeader, IonPage, IonRow, IonTitle, IonToolbar } from '@ionic/react';
import ExploreContainer from '../components/ExploreContainer';
import './Home.css';
import { useState } from 'react';

const Home: React.FC = () => {
  const [imageUrl, setImageUrl] = useState("https://t3.ftcdn.net/jpg/02/48/42/64/360_F_248426448_NVKLywWqArG2ADUxDq6QprtIzsF82dMF.jpg")
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Image Cleaning</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <img style={{ width: "100%", height: "80%" }} src={imageUrl}></img>
        <IonGrid>
          <IonRow>
            <IonCol size="6">
              <IonButton style={{ width: "100%" }} color="danger">No</IonButton>
            </IonCol>
            <IonCol size="6">
              <IonButton style={{ width: "100%" }} color="success">Yes</IonButton>
            </IonCol>
          </IonRow>
        </IonGrid>
      </IonContent>
    </IonPage>
  );
};

export default Home;
