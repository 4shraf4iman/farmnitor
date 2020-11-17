
import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import {AngularFireAuth} from 'angularfire2/auth';
import firebase from 'firebase'
import {AngularFireDatabase,FirebaseListObservable} from 'angularfire2/database-deprecated';
@Component({
  selector: 'page-hello-ionic',
  templateUrl: 'hello-ionic.html'
})

export class HelloIonicPage {
  reference:any;
  mytext:any;
  test:Array=[];
  exe:FirebaseListObservable;

  constructor( public navCtrl: NavController, private fire:AngularFireAuth,public db:AngularFireDatabase) {
    
    this.exe=db.list('/Moisture');
  }

  addData(){
    this.reference=firebase.database().ref('/example')

    this.reference.push({
      example:this.mytext
    })
    console.log("data added");
  }

  getdata(){
    this.reference=firebase.database().ref('/Moisture')
    this.db.list(this.reference).subscribe(suject=>{
      this.test=suject;
      console.log("subject"+suject);
    });
  }

}
