import { Component } from '@angular/core';
import { AuthService } from './auth.service';

@Component({
    selector: 'app-login',
    moduleId: module.id,
    templateUrl: 'auth.component.html'
})
export class AuthComponent {
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
        }else{
            // authenticate if token present
        }
    }

}
