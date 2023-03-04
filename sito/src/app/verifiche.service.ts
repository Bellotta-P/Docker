import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AppSettings } from './appSetting';


@Injectable({
  providedIn: 'root'
})
export class VerificheService {

  private baseUrlPrin = AppSettings._API;


  private baseUrl = this.baseUrlPrin + 'Verifiche';

  constructor(private http: HttpClient) { }

  getVerificheList(): Observable<any> {
    return this.http.get(`${this.baseUrl}`);
  }
}