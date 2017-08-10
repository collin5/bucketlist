import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service';

@Component({
    selector: 'app-login',
    moduleId: module.id,
    templateUrl: 'login.component.html'
})
export class LoginComponent {
    private error_msg: string = "";
    constructor(private _auth: AuthService){}

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

    private authenticate(data: any): void{
        if (data.hasOwnProperty('error_msg')){
            this.error_msg = data['error_msg'];
        }
    }

}
