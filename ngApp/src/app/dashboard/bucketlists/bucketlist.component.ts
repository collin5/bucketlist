declare var UIkit: any;

import { Component } from '@angular/core';
import { BucketlistService } from './bucketlist.service';

@Component({
    selector: 'dash-bucketlists',
    moduleId: module.id,
    templateUrl: 'bucketlists.component.html',
    providers: [ BucketlistService ]
})
export class Bucketlists{

    constructor(private _bucketService: BucketlistService){}

    title: string = 'My bucketlists';
    add_bucket__err: string = null;

    showAddSpinner = false;

    onAdd(title, desc): void{
        this.showAddSpinner = true;
        this._bucketService.addBucket(title, desc).subscribe(
            $data => {
                if ($data.hasOwnProperty('error_msg')){
                    UIkit.notification($data['error_msg'], {status: 'danger'});
                }else{
                    let $msg = ($data.hasOwnProperty('success_msg'))? $data['success_msg']: 'An error occured !';
                    UIkit.modal('#add-bucket__modal').hide();
                    UIkit.notification($msg, { status: 'success' });
                }
                this.showAddSpinner = false;
            },
            error => {
                if (error.hasOwnProperty('error_msg')){
                    this.add_bucket__err = error['error_msg']
                }
                this.showAddSpinner = false;
            },
        )
    }
}
