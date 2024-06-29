import { Component, OnInit } from '@angular/core';
import { BackendCallsService } from '../backend-calls.service';

@Component({
  selector: 'app-vendor-list',
  templateUrl: './vendor-list.component.html',
  styleUrl: './vendor-list.component.css'
})
export class VendorListComponent implements OnInit{
  vendors= [{id:0,name:'',ratings:1,place:'',phone_number:''}]
  constructor(private backend:BackendCallsService) {
      //
  }
  ngOnInit(): void {
    this.pageInit();
  }
  pageInit(){
    this.backend.readAll()
    .subscribe({
      next:(vendors:any) => {
        this.vendors = [...vendors];
        console.log(vendors);
      },
      error:(err)=>{
        console.log(err)
      }

    })
  }

  doDelete(id:any) {
    this.backend.delete(id)
      .subscribe({
        next:(json:any)=>{
          alert(json.message);
          this.pageInit();
        },
        error:(err) => { 
          console.log(err)
        }
      })
  }
}
