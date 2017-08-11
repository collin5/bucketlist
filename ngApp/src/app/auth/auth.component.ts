import { Component } from '@angular/core';
import { AuthService } from './auth.service';
import { Router } from '@angular/router';

@Component({
    selector: 'app-login',
    moduleId: module.id,
    templateUrl: 'auth.component.html'
})
export class AuthComponent {
    private error_msg: string = "";
    constructor(private _auth: AuthService, private _router: Router){}

    onLogin(username, passphrase): void{
        this._auth.getToken(username, passphrase).subscribe(
            data => this.authenticate(data),
            error => {
                if (error.hasOwnProperty('error_msg')){
                    this.error_msg = error['error_msg']
                }
            } 
        )
    }

    onRegister(username, email, passphrase): void{
        this._auth.registerUser(username, email, passphrase).subscribe(
            data => {
                console.log(JSON.stringify(data));
            },
            error =>{
                if (error.hasOwnProperty('error_msg')){
                    this.error_msg = error['error_msg'];
                }
            }
        )
    }

    private authenticate(data: any): void{
        if (data.hasOwnProperty('error_msg')){
            this.error_msg = data['error_msg'];
        }else{
            // get token if exists and redirect to dashboard
            if (data.hasOwnProperty('token')){
                localStorage.setItem('token', data['token']);
                // then redirect to dashboard
                this._router.navigate(['/dashboard']);
            }
        }
    }

}
