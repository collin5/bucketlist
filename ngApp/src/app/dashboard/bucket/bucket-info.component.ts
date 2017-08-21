import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
    selector: 'bt-info',
    moduleId: module.id,
    templateUrl: 'bucket-info.component.html'
})
export class BucketInfoComponent{
    title: string = "Bucket info";
    bucket_title: string = "Bucket title";
    private _id: number | string;

    constructor(private _route: ActivatedRoute){
        this._id = this._route.snapshot.params['id']
    }
}
