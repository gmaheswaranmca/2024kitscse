import { Component, OnInit } from '@angular/core';
import { BackendCallsService } from '../backend-calls.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-vendor-edit',
  templateUrl: './vendor-edit.component.html',
  styleUrl: './vendor-edit.component.css'
})
export class VendorEditComponent implements OnInit{
  id:any = 0
  vendor:any = {
    name:'',
    ratings:1,
    place:'',
    phone_number:''
  };
  constructor(private backend:BackendCallsService,
      private _router:Router,
      private _route: ActivatedRoute) {
        //
  }
  
  ngOnInit(): void {
    this.id = this._route.snapshot.paramMap.get('id')
    this.backend.readById(this.id)
      .subscribe({
          next:(vendor)=>{
            this.vendor = { ... vendor }
          },
          error: (err) => {
            console.log(err)
          }
      })
  }

  doUpdate() {
    this.backend.update(this.id,this.vendor)
      .subscribe({
        next:(vendor)=>{
          console.log(vendor)
          this._router.navigate(['vendors/list'])
        }, 
        error:(err)=>{
          console.log(err)
        }       
      })
  }
}
