import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-registration',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registerForm: FormGroup;

  constructor(private formBuilder: FormBuilder) { 
    
    this.registerForm = this.formBuilder.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      confirmPassword: ['', Validators.required],
      dob: ['', Validators.required]
    }, {
      validator: [this.passwordMatchValidator]
    });
  }

  ngOnInit() {
  
  }

 
  

  passwordMatchValidator(group: FormGroup) {
    const password = group.controls['pasword']?.value;
    const confirmPassword = group.controls['confirmPassword']?.value;

    return password === confirmPassword ? null : { passwordMismatch: true };
  }

  Submit() {
    if (this.registerForm.valid) {
    
      console.log('Formulario de registro válido:', this.registerForm.value);
    } else {

      console.log('Formulario de registro inválido:', this.registerForm.errors);
    }
  }
}