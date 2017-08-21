import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';

@Component({
    selector: 'app-bucket',
    moduleId: module.id,
    templateUrl: 'bucket.component.html'
})
export class Bucket{
    @Input() title: string;
    @Input() description: string;


    constructor(private _router: Router){
    }

    onClick(): void{
        this._router.navigate(['/dashboard/bucket/info'])
    }
}
