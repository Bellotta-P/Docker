


import { Observable } from "rxjs";
import { Component, OnInit } from "@angular/core";
import { Router } from '@angular/router';
import {Location} from '@angular/common'
import { Docenti, Verifiche } from "../models/data";
import { VerificheService } from "../verifiche.service";

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent  implements OnInit {
  data: Verifiche[] = undefined!;
  obsRooms: Observable<Verifiche[]> | undefined
  t:any;

  constructor(private veri: VerificheService,private router: Router,private location: Location ) { }

  ngOnInit() {
    this.reloadData();
  }

  reloadData() {
    this.obsRooms = this.veri.getVerificheList()
    this.obsRooms.subscribe(this.fati)
  }
  fati = (data: Verifiche[]) => {
    this.data = data;
  }

  logout()  {
    // Clear session data
    this.t = localStorage.removeItem('user');
    this.router.navigate(['/login']);
  }
}