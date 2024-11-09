import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http:HttpClient) {

   }

   login(data:any):Observable<any>{
    return this.http.post('http://localhost:8000/login/',data);
   }


   

}
