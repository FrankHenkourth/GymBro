import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../Services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent implements OnInit {
 
  loginForm:FormGroup
 
  ngOnInit(): void {
    
  }
  constructor(private fb:FormBuilder,
    private auth:AuthService
  ){
    this.loginForm =fb.group(
      {username: ['',[Validators.required]],
        password:['',[Validators.required]]
      }
    )
  }
  Submit(){
    if(this.loginForm.valid){
      this.auth.login({
        username: this.loginForm.controls['username'].value,
        password: this.loginForm.controls['password'].value
      }).subscribe(
        (response) => {
          // Manejar la respuesta exitosa
          console.log('Respuesta:', response);
        },
        (error) => {
          // Manejar el error
          console.error('Error:', error);
        }
      );
    }
  }

}
