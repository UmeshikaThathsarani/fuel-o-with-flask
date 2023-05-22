import React from 'react';
import { Card } from 'antd';

import './rent.css';

const { Meta } = Card;

function Rent() {
  return(
    <div className="row">
      <div className="column">
        <a href="https://www.facebook.com/costarentacarsgalle/" target="blank" style={{display: "table-cell"}}>
          <Card
              hoverable
              style={{ width: "100%" }}
              cover={
              <img style={{height: "230px", width: "350px", overflow: "hidden" }} alt="CostaRentACar" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuckQaYHD6FijHmYygGAdwtftWZ8baax_4AhNvRJWl4w&usqp=CAU&ec=48600112" />}
              >
              <Meta title="Costa Rent A Car - Galle" description=
              {
                <p>
                  Vehicle Types: Van, Car, Scooty <br />
                  Contacts: +94 77 747 8048 <br />
                  With Driver or Without Driver
                </p>
              }
               />
            </Card>
          </a>
      </div>
      <div className="column">
        <a href="https://www.facebook.com/profile.php?id=100089064541837" target="blank" style={{display: "table-cell"}}>
          <Card
              hoverable
              style={{ width: "100%" }}
              cover={
              <img style={{height: "230px", width: "350px", overflow: "hidden" }} alt="ShaGaTransport" src="https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-6/331057093_544313354461617_4233519779338726362_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeFU5mX45dRzUJpFy09CD0MEO3h2L5NYaAE7eHYvk1hoAdybpV57CBaTGNiiiSyavPkXJzXbx4cbxaiA0LEYOzG_&_nc_ohc=1cEWAmF5G40AX8WfQFf&_nc_ht=scontent-ord5-1.xx&oh=00_AfA6IKj-unQFnTfazvFa1XibkWPF1AGFxo105RjFrzT1wQ&oe=64702847" />}
              >
              <Meta title="ShaGa Transport - Galle" description={
                <p>
                  Vehicle Types: Van, Car, Bus <br />
                  Contacts: +94 76 313 3332 <br />
                  Tour and Transport
                </p>
              }
               />
            </Card>
          </a>
      </div>
      <div className="column">
        <a href="https://gallecabs.lk/" target="blank" style={{display: "table-cell"}}>
          <Card
              hoverable
              style={{ width: "100%" }}
              cover={
              <img style={{height: "230px", width: "350px", overflow: "hidden" }} alt="GalleCabs" src="https://scontent-ord5-2.xx.fbcdn.net/v/t1.6435-9/179992570_106317658281405_3579268240145201779_n.png?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeGAhh1eHo5ok5LzeAN659qE43Hdl9NGuU7jcd2X00a5TgkgufU15-v6rZxJkOlV11ykEs9VPhjpsJ3zZRqUyalt&_nc_ohc=Lt6IUJO_LtkAX-69sdd&_nc_ht=scontent-ord5-2.xx&oh=00_AfBeHpWc9_-3UfBTTei-AYQJY7xxRLjreuvkX12UgRMXXw&oe=6492F18A" />}
              >
              <Meta title="Galle Cabs (PVT) LTD - Galle"
               description={
                <p>
                  Vehicle Types: Bike, Van, Car, Bus <br />
                  Contacts: +94 76 581 0045 <br />
                  Car Rental Daily, Weekly, Monthly & Long term
                </p>
              }
               />
            </Card>
          </a>
      </div>

    </div>
  )
}

export default Rent;
