function VWIN=WIN(Gato)
    VWIN=0;
    W=(Gato==1);
    if( (W(1)==1) && (W(2)==1) && (W(3)==1) ||...
        (W(4)==1) && (W(5)==1) && (W(6)==1) ||...
        (W(7)==1) && (W(8)==1) && (W(9)==1) ||...
        (W(1)==1) && (W(4)==1) && (W(7)==1) ||...
        (W(2)==1) && (W(5)==1) && (W(8)==1) ||...
        (W(3)==1) && (W(6)==1) && (W(9)==1) ||...
        (W(1)==1) && (W(5)==1) && (W(9)==1) ||...
        (W(3)==1) && (W(5)==1) && (W(7)==1) )
            VWIN=1;
    else
        W=(Gato==2);
        if( (W(1)==1) && (W(2)==1) && (W(3)==1) ||...
        (W(4)==1) && (W(5)==1) && (W(6)==1) ||...
        (W(7)==1) && (W(8)==1) && (W(9)==1) ||...
        (W(1)==1) && (W(4)==1) && (W(7)==1) ||...
        (W(2)==1) && (W(5)==1) && (W(8)==1) ||...
        (W(3)==1) && (W(6)==1) && (W(9)==1) ||...
        (W(1)==1) && (W(5)==1) && (W(9)==1) ||...
        (W(3)==1) && (W(5)==1) && (W(7)==1) )
            VWIN=2;
        end
    end
end