import { Component} from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
    selector: 'bt-info',
    moduleId: module.id,
    templateUrl: 'bucket-info.component.html'
})
export class BucketInfoComponent{
    title: string = "Bucket info";
    bucket_title: string = "Bucket title";
    private _id: number;

    bucketItemAddDate: string;

    // TODO:  get info from api
    bucket_info: boolean = true;

    constructor(private _route: ActivatedRoute, private _router: Router){
        this._id = this._route.snapshot.params['id'];
        if (typeof this._id == undefined || this._id < 1){
            this._router.navigate(['/dashboard']);
        }
    }

    onAdd(title, notes): void{
        alert(this.bucketItemAddDate);
    }

}
