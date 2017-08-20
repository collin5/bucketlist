declare var UIkit: any;

import { Component, OnInit } from '@angular/core';
import { BucketlistService } from './bucketlist.service';
import { IBucket } from './bucket';

@Component({
    selector: 'dash-bucketlists',
    moduleId: module.id,
    templateUrl: 'bucketlists.component.html',
    providers: [ BucketlistService ]
})
export class Bucketlists implements OnInit{

    constructor(private _bucketService: BucketlistService){}

    title: string = 'My bucketlists';
    add_bucket__err: string = null;

    listNew: IBucket[];

    showAddSpinner = false;

    ngOnInit(): void{
        this.getList();
    }

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
                    this.listNew = [];
                    this.getList();
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

    getList(): void{
        this._bucketService.getBucketlists().subscribe(
            $data => this.listNew = $data,
            $error =>{
                UIkit.notification($error, {status: 'danger'})
            }
        )
    }
}
